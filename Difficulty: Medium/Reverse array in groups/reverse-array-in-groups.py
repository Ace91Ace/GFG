class Solution:
    def reverseingroups(self, arr, k):
        stk = []
        for i in range(len(arr)):
            if len(stk) == k:
                for j in range(len(stk)):
                    arr[i - k + j] = stk.pop()
            stk.append(arr[i])
        m = len(stk)
        for j in range(m):
            arr[len(arr) - m + j] = stk.pop()
