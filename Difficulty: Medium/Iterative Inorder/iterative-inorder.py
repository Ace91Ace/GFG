#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        # code here
        stk = []
        curr = root
        res = []
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.data)
            curr = curr.right
        return res