from functools import lru_cache
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        @lru_cache(None)
        def fib(x):
            if x == 0:
                return 0
            if x <= 1:
                return 1
            return fib(x-1) + fib(x-2)
        return fib(n)
        
