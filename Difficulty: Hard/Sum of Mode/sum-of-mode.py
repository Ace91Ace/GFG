import heapq

class Solution:
    def sumOfModes(self, arr, k):
        def calculateMode():
            while theap and -theap[0][0] != dic.get(theap[0][1], 0):
                heapq.heappop(theap)
            return theap[0][1] if theap else 0

        n = len(arr)
        sm, l, lx = 0, 0, 0
        dic, theap = {}, []
        for r in range(n):
            dic[arr[r]] = dic.get(arr[r], 0) + 1
            heapq.heappush(theap, (-dic[arr[r]], arr[r]))
            lx += 1
            while lx > k:
                dic[arr[l]] -= 1
                if dic[arr[l]] == 0:
                    del dic[arr[l]]
                l += 1
                lx -= 1
            if lx == k:
                sm += calculateMode()
        return sm