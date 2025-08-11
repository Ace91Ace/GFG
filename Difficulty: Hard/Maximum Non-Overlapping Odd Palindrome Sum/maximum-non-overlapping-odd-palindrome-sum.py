import heapq

class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # ---------- Step 1: Manacher's algorithm (odd-length only) ----------
        # d1[i] = radius of longest odd palindrome centered at i
        # palindrome length = 2 * d1[i] - 1
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # Store palindrome center data: (start_index, center_index, end_index)
        centers = [(i - d1[i] + 1, i, i + d1[i] - 1) for i in range(n)]

        # ---------- Step 2: Longest palindrome ending at each position ----------
        left_best_end = [0] * n
        heap = []  # (center_index, right_end)
        for end in range(n):
            # Add the center whose index matches the current end
            ci = end
            _, center, right_end = centers[ci]
            heapq.heappush(heap, (center, right_end))

            # Remove centers that end before current position
            while heap and heap[0][1] < end:
                heapq.heappop(heap)

            # If any valid palindrome covers 'end', compute its length
            if heap:
                min_center = heap[0][0]
                left_best_end[end] = 2 * (end - min_center) + 1

        # ---------- Step 3: Longest palindrome starting at each position ----------
        right_best_start = [0] * n
        centers_sorted = sorted(centers, key=lambda x: x[0])
        heap2 = []  # max-heap by center index (-center_index, right_end)
        idx = 0
        for start in range(n):
            # Add all centers that start before or at current position
            while idx < n and centers_sorted[idx][0] <= start:
                _, center, right_end = centers_sorted[idx]
                heapq.heappush(heap2, (-center, right_end))
                idx += 1

            # Remove centers that end before current position
            while heap2 and heap2[0][1] < start:
                heapq.heappop(heap2)

            # If valid palindrome covers 'start', compute its length
            if heap2:
                max_center = -heap2[0][0]
                right_best_start[start] = 2 * (max_center - start) + 1

        # ---------- Step 4: Prefix/suffix maximums ----------
        left_max = [0] * n
        left_max[0] = left_best_end[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], left_best_end[i])

        right_max = [0] * n
        right_max[-1] = right_best_start[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], right_best_start[i])

        # ---------- Step 5: Combine results ----------
        ans = 0
        for cut in range(n - 1):
            ans = max(ans, left_max[cut] + right_max[cut + 1])

        return ans