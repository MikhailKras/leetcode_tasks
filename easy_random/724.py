class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum, i, n = 0, sum(nums) - nums[0], 0, len(nums)
        while i + 1 < n:
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
            r_sum -= nums[i + 1]
            i += 1
        else:
            if l_sum == r_sum:
                return i
        return -1

