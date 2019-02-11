'''
Given a linked list change it in sorted order
Merge sort
1. if head is null
one element in the linked list then return
2. else divide linked list in two halves
3. Sort the two halves
MergeSort(a)
MergeSort(b)
4. Merge the sorted a and b and
update the header pointer using
headRef
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class MergeSort:

    def __init__(self):
        self.head = None

    def get_mid(self, head, end):

        # cursor is at head
        current = head
        size = 0
        # loop through the linked list
        for i in range(0, size/2):
            current = current.next

        return current

    def sort(self, head, end=None):
        if head is end: return head

        if end is not None:
            end.next =  None

        mid = self.get_mid(head, end)
        head2 = sort(mid.next, end, level+1)






