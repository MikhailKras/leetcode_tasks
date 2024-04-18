class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(cur, opened, closed, n):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if opened < n:
                helper(cur + '(', opened + 1, closed, n)
            if closed < opened:
                helper(cur + ')', opened, closed + 1, n)
        
        helper('', 0, 0, n)
        return res
        
