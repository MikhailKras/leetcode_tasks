class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        nums, l, r = sorted(nums), 0,  len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                res += r - l
                l += 1
            else:
                r -= 1
        return res

