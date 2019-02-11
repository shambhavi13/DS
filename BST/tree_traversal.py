'''
Inorder Traversal
1. traverse the left subtree
2. visit the root
3. traverse the right subtree
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# func to do in order traversal
def printInorder(root):

    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreoder(root):

    if root:
        print(root.val)
        printPreoder(root.left)
        printPreoder(root.right)

def printPostorder(root):

    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)