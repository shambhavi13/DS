'''
Given a binary tree return level
order of traversal left to right, level by level
 3
/ \
9  20
   / \
 15  7

order of traversal
[
[3]
[9, 20],
[15, 7]
]
'''

class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class solution:

    def levelorder(self, root):

        """
        :param root: tree node
        :return: list of list of integers
        """
        result = []
        if not root: return result

        cur_level = [root]
        # loop until empty
        while cur_level != []:
            vals = []
            new_level = []
            for node in cur_level:
                vals.append(node.data)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            result.append(vals)
            cur_level = new_level
        return result