# Calculate the length of linked list

"""
Calculate kth to last Node
"""

class Node:

    def __init__(self, val):

        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def _append(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node:
            last_node = last_node.next
        # append
        last_node.next = new_node

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def _kth_last(self,k):
        """
        Calculate length of linked list
        Count total length until nth element
        :return:
        """

        total = self.len_iterative()
        cur = self.head

        if cur is None : return

        # while cur is not null
        while cur:
            if total == k:
                print(cur.data)
                return cur
            # if not decrement total list
            # move along the current list
            total -= 1
            cur = cur.next



if __name__ == "__main__":

    llist = LinkedList()
    llist._append("A")
    llist._append("B")
    llist._append("C")
    llist._append("D")

    print(llist._kth_last(2))


