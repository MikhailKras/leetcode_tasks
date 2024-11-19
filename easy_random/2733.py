class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.pop(nums.index(min(nums)))
        if nums:
            nums.pop(nums.index(max(nums)))
        return -1 if not nums else nums[0]

