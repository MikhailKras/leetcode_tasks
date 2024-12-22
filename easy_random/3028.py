class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            cur += num
            if cur == 0:
                res += 1
        return res
        
