from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sm = sorted_nums[left] + sorted_nums[right]
            if sm == target:
                ans = sorted_nums[left], sorted_nums[right]
                break
            elif sm > target:
                right -= 1
            else:
                left += 1
        for i in range(len(nums)):
            if nums[i] == ans[0]:
                l = i
                break
        for i in range(len(nums)):
            if nums[i] == ans[1]:
                r = i

        return l, r
