class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums, n = sorted(nums), len(nums)
        seen = {}
        for i in range(n):
            if sorted_nums[i] not in seen:
                seen[sorted_nums[i]] = i
        
        res = []
        for i in range(n):
            res.append(seen[nums[i]])
        return res

