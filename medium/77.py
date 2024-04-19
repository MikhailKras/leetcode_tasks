class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(cur, start):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(start, n + 1):
                helper(cur + [i], i + 1)
        
        helper([], 1)
        return res

