from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if k > 0 and nums[k - 1] == nums[k]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                sm = nums[i] + nums[j]
                if sm == -nums[k]:
                    ans = [nums[i], nums[j], nums[k]]
                    res.append(ans)
                    while i < j and nums[i] == ans[0]:
                        i += 1
                    while i < j and nums[j] == ans[1]:
                        j -= 1
                elif sm > -nums[k]:
                    j -= 1
                else:
                    i += 1

        return res
