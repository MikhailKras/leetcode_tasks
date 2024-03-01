class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_diff, diff, max_i = 0, 0, 0
        for i in range(1, len(nums) - k + 1):
            diff += nums[i + k - 1] - nums[i - 1]
            if nums[i + k - 1] - nums[i - 1] > 0:
                if max_diff < diff:
                    max_diff, max_i = diff, i
        return sum(nums[max_i:max_i + k]) / k

