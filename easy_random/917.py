class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res, n = "", len(s)
        l, r = 0, n - 1
        while len(res) < n:
            if s[l].isalpha():
                while not s[r].isalpha():
                    r -= 1
                res += s[r]
                r -= 1
            else:
                res += s[l]
            l += 1
        return res
        
