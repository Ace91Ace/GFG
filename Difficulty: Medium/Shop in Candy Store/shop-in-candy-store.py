import heapq

class Solution:
    def minMaxCandy(self, prices, k):
        # code here'
        n = len(prices)
        prices.sort()
        mn, mx = 0, 0
        count = 0
        for i in range(n):
            mn += prices[i]
            count += (1 + k)
            if count >= n:
                break
        count = 0
        prices = prices[::-1]
        for i in range(n):
            mx += prices[i]
            count += (1 + k)
            if count >= n:
                break
        return [mn, mx]
        