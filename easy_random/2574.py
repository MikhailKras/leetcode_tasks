from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        n = len(nums)
        for i in range(n - 1):
            left_sum.append(left_sum[i] + nums[i])

        right_sum = [0]
        rev_nums = nums[::-1]
        for i in range(n - 1):
            right_sum.append(right_sum[i] + rev_nums[i])
        right_sum = right_sum[::-1]
        return [abs(l - r) for l, r in zip(left_sum, right_sum)]
