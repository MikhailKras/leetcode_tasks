class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        incr = False
        decr = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                decr = True
            elif nums[i] < nums[i + 1]:
                incr = True
        return not (decr and incr)
        
