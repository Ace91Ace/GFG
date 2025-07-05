class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
		#Code here
		par = [i for i in range(V)]
		def find(u):
		    if u != par[u]:
		        par[u] = find(par[u])
		    return par[u]
		
		def union(u,v):
		    pu = find(u)
		    pv = find(v)
		    
		    if pu == pv:
		        return True
		    par[pu] = pv
		    return False
		
		vis = set()
		for u in range(V):
		    for v in adj[u]:
		        if (v, u) in vis:
		            continue
		        vis.add((u,v))
		        if union (u,v):
		            return 1
		return 0
		    
		    