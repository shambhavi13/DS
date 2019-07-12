#Queue implementation

class Queue:

    def __init__(self):
        self.items= [] # list for queue

    def _is_empty(self):
        return self.items == [] # see if list is empty

    def _en_queue(self, item):
        self.items.insert(0, item) # insert at the end of queue O(n) operation

    def _de_queue(self):
        return self.items.pop()  # del from the front O(1) operation

    def _size(self):
        return len(self.items)  # len of list


q = Queue()
q._en_queue(4)
q._en_queue("dog")
q._en_queue(True)
print(q._size())