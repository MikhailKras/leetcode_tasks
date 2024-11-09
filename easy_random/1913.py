class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_max = nums.pop(nums.index(max(nums)))
        second_max = max(nums)
        first_min = nums.pop(nums.index(min(nums)))
        second_min = min(nums)
        return first_max * second_max - first_min * second_min

