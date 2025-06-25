class Solution:
    def minChar(self, s):
        #Write your code here
        def help(s):
            temp = s + '#' + s[::-1]
            lps = [0] * len(temp)
        
            for i in range(1, len(temp)):
                l = lps[i - 1]
                while l > 0 and temp[i] != temp[l]:
                    l = lps[l - 1]
                if temp[i] == temp[l]:
                    l += 1
                lps[i] = l
        
            return s[:lps[-1]]

        x = len(help(s))
        return len(s)-x
        