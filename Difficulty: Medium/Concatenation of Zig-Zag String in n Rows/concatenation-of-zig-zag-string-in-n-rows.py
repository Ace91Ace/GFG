class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def cols(s):
            if numRows == 1:
                return len(s)
            count = 0
            y = 0
            n = len(s)
            while count < n:
                count += numRows
                y += 1
                if count < n:
                    diag = numRows - 2
                    count += diag
                    y += diag
            return y
        col = cols(s)
        n = len(s)
        x = [[-1]*col for _ in range(numRows)]
        flag = True
        c, r, j = 0, 0, 0
        while j < n:
            if flag:
                for i in range(numRows):
                    if j >= n: break
                    x[i][c] = s[j]
                    j += 1
                flag = False
                c += 1
            else:
                for i in range(numRows-2, 0, -1):
                    if j >= n: break
                    x[i][c] = s[j]
                    j += 1
                    c += 1
                flag = True
        res = [[i for i in m if i != -1] for m in x]
        z = ""
        for i in res:
            z += "".join(i)
        return z
