class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(cur, remains):
            if remains == []:
                res.append(cur)
                return
            for i in range(len(remains)):
                helper(cur + [remains[i]], remains[:i] + remains[i + 1:])
        helper([], nums)
        return res

