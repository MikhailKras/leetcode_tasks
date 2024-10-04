class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def helper(cur: str, i: int) -> None:
            if i == n:
                res.append(cur)
                return
            if cur and cur[-1] == '1' or not cur:
                helper(cur + '0', i + 1)
            helper(cur + '1', i + 1)
        
        helper('', 0)
        return res

