class Solution:
    def is_arithmetic(self, nums: List[int]) -> bool:
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != diff:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [self.is_arithmetic(nums[ll:rr + 1]) for ll, rr in zip(l, r)]

