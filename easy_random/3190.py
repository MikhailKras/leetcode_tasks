class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            remain = num % 3
            res += min(remain, 3 - remain)
        return res
        
