class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = nums[1]
        if len(nums) > 2:
            dp[2] = nums[2] + dp[0]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        
        return max(dp[len(nums) - 2:])

