#User function Template for python3
from heapq import*
class Solution:
    def topKSumPairs(self, A, B, k):
        n=len(A)
        m=len(B)
        res=[]
        A.sort(reverse=True)
        B.sort(reverse=True)
        seen=set()
        heap=[]
        heappush(heap,(-A[0]-B[0],0,0))
        seen={(0,0)}
        while(k):
            val,i,j=heappop(heap)
            k-=1
            res.append(-val)
            if(i+1<n and (i+1,j) not in seen):
                heappush(heap,(-A[i+1]-B[j],i+1,j))
                seen.add((i+1,j))
            if(j+1<m and (i,j+1) not in seen):
                heappush(heap,(-A[i]-B[j+1],i,j+1))
                seen.add((i,j+1))
        return res