class Solution:
    def asciirange(self, s):
        n = len(s)
        occ = [[-1, -1] for _ in range(26)]
        p = 0
        for i, x in enumerate(s):
            p += ord(x)
            idx = ord(x) - ord('a')
            if occ[idx][0] == -1:
                occ[idx][0] = p
            else:
                occ[idx][1] = p - ord(x)
        res = []
        for i in occ:
            if i[1] != -1 and i[1] != i[0]:
                res.append(i[1]-i[0])
        return res
