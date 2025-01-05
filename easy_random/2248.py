class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        i = 1
        res = set(nums[0])
        while i < len(nums):
            res = res.intersection(set(nums[i]))
            i += 1
        return sorted(res)

