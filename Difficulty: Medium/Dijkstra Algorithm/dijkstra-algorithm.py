
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here\
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
            
        q = []
        heapq.heappush(q, [0,src])
        vis = [float('inf')]*V
        vis[src] = 0
        
        while q:
            d, node = heapq.heappop(q)
            if d > vis[node]:
                continue
            for nei, w in adj[node]:
                if vis[nei] > vis[node] + w:
                    vis[nei] = vis[node] + w
                    heapq.heappush(q, [vis[nei], nei])
        return vis
        