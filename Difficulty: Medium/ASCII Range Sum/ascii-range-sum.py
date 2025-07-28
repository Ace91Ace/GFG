class Solution:
    def asciirange(self, s):
        n = len(s)
        occ = [[-1, -1] for _ in range(26)]
        pref = [0] * n
        p = 0
        for i, x in enumerate(s):
            p += ord(x)
            pref[i] = p
            idx = ord(x) - ord('a')
            if occ[idx][0] == -1:
                occ[idx][0] = i
            else:
                occ[idx][1] = i
        res = []
        for i in range(26):
            start, end = occ[i]
            if start != -1 and end != -1 and end > start + 1:
                y = pref[end-1] - pref[start]
                if y:
                    res.append(y)
        return res
