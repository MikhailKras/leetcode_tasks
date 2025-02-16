class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            left = nums[i - k] if i - k >= 0 else 0
            right = nums[i + k] if i + k < len(nums) else 0
            if nums[i] > max(left, right):
                res += nums[i]
        return res

