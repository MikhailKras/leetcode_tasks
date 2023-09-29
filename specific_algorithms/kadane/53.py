class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = 0
        res = min(nums)
        for i in range(len(nums)):
            max_end += nums[i]
            res = max(res, max_end)
            if max_end < 0:
                max_end = 0
        return res
        
