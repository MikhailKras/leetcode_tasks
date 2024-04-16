class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def helper(cur, i):
            if i == n:
                res.append(cur)
                return
            if s[i].isdigit():
                helper(cur + s[i], i + 1)
            else:
                helper(cur + s[i].lower(), i + 1)
                helper(cur + s[i].upper(), i + 1)
        
        helper('', 0)
        return res

