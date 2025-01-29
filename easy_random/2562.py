class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        while len(nums) > 1:
            res += int(str(nums.pop(0)) + str(nums.pop()))
        if nums:
            res += nums[0]
        return res

