class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pref_sum = [0]
        for i in range(len(nums)):
            pref_sum.append(pref_sum[i] + nums[i])
        
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res += pref_sum[i + 1] - pref_sum[start]
        
        return res
        

