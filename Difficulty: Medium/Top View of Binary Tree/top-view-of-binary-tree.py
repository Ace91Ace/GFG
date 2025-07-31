from collections import deque
class Solution:
    def topView(self, root):
        q = deque([(root, 0)])
        dic = {}
        while q:
            node, d = q.popleft()
            if d not in dic:
                dic[d] = node
            if node.left:
                q.append((node.left, d - 1))
            if node.right:
                q.append((node.right, d + 1))
        res = [[i, dic[i]] for i in dic]
        res.sort()
        res = [i[1].data for i in res]
        return res
