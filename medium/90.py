class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        nums.sort()
        
        def helper(cur, i):
            res.append(cur)
            if i >= n:
                return
            helper(cur + [nums[i]], i + 1)
            helper(cur, i + 1)
        
        helper([], 0)
        return list(set(map(tuple, res)))

