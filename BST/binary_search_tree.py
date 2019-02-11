'''
Create binary search tree
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        '''
        insert data into BST
        :return:
        '''

        if self.data == data:
            return False # as bst cannot have duplicate data

        elif data < self.data:
            '''
            data less than root data is placed on
            left side 
            '''

            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True

        else:
            '''
            data greater than root data is placed on
            right side
            '''
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True

    def delete(self, data):
        '''
        deleting node
        :param data:
        :return:
        '''
        if data < self.data:
            self.leftchild = self.leftchild.delete(data)
        elif data> self.data:
            self.rightchild = self.rightchild.delete(data)
        else:
            # deleting node with one child
            if self.leftchild is None:
                temp = self.rightchild
                self = None
                return temp
            elif self.rightchild is None:
                temp = self.leftchild
                return temp
        return self

class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)
        else:
            return False

# driver program

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree)

    ''' Following tree is getting created:
                        10
                     /      \
                   5         12
                  / \           \
                4     8          20
                     /          /
                    7         15
                             /
                           13
    '''

    print('\n\nAfter deleting 20')
    tree.delete(20)







