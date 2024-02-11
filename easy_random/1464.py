class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxs = [-1, -1]
        for num in nums:
            if num > maxs[0]:
                maxs[0], maxs[1] = num, maxs[0]
            elif num > maxs[1]:
                maxs[1] = num
        return (maxs[0] - 1) * (maxs[1] - 1)
        
