class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        j = 0
        while j < k:
            min_index = nums.index(min(nums))
            nums[min_index] = nums[min_index] * multiplier
            j += 1
        return nums
            
