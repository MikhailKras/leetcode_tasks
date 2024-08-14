class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        nulls = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nulls.append(nums.pop(i))
                i -= 1
            i += 1
        return nums + nulls

