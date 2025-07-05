from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        q = deque([0])
        vis = set([0])
        res = [0]
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)
                    res.append(nei)
        return res
        