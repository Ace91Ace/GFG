#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # code here
        stk1, stk2 = [root], []
        
        while stk1:
            node = stk1.pop()
            stk2.append(node)
            
            if node.left:
                stk1.append(node.left)
            if node.right:
                stk1.append(node.right)
            
        return [node.data for node in stk2[::-1]]