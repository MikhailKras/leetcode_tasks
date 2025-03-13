class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l_even, r_even = nums[0] % 2 == 0, sum(nums[1:]) % 2 == 0
        if (l_even + r_even) % 2 == 0:
            return len(nums) - 1
        return 0
        

