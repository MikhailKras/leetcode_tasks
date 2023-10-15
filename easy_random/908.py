class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num, min_num = nums[0], nums[0]
        for num in nums:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
        max_num_new, min_num_new = max_num - k, min_num + k
        if max_num_new >= min_num_new:
            return max_num_new - min_num_new
        else:
            return 0
        
