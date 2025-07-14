'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        # code here
        stk, res = [root], []
        
        while stk:
            node = stk.pop()
            res.append(node.data)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        return res
            