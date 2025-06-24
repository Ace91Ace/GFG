from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        c1 = Counter(s)
        c = [c1[i] for i in c1]
        if len(set(c)) > 2:
            return False
        c2 = Counter(c)
        if len(set(c)) == 1:
            return True
        if 1 in c2 and c2[1] == 1:
            return True
        if len(c2) == 2:
            (f1, n1), (f2, n2) = c2.items()
            if abs(f1 - f2) == 1 and ((f1 > f2 and n1 == 1) or (f2 > f1 and n2 == 1)):
                return True
        return False
