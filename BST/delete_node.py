'''
find the min value node
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def minValNode(self, node):
        current = node

        # loop to find leftmost leaf
        while(current.leftchild is not None):
            current = current.leftchild

        return current

    '''
    delete a node
    1. if current node data is less than root node
    search only left subtree else search right subtree
    2. deleting node with one child
    leftchild --> None
    return rightchild
    rightchild --> None
    return rightchild
    '''

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




