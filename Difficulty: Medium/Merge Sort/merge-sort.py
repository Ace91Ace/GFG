class Solution:
    def mergeSort(self, arr, l, r):
        def mrg(arr, l, r, m):
            n1 = m - l + 1
            n2 = r - m
            L = arr[l:m+1]
            R = arr[m+1:r+1]
            i = j = 0
            k = l
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        def srt(arr, l, r):
            if l < r:
                mid = (l + r) // 2
                srt(arr, l, mid)
                srt(arr, mid + 1, r)
                mrg(arr, l, r, mid)
            return arr
        return srt(arr, l, r)
