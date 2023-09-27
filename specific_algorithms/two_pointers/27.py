from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            if nums[0] == val:
                nums[0] = '-'
                return 0
            return 1
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != val:
                l += 1
            r += 1
        while l < len(nums) and nums[l] != val:
            l += 1
        return l
