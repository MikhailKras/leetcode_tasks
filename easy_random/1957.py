class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if len(res) < 2 or res[-1] != res[-2] or res[-2] != s[i]:
                res.append(s[i])
        return "".join(res)

