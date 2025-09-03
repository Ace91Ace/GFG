class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        return 2*(2**(n-1)) -1