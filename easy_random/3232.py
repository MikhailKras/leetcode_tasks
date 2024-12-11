class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if num < 10:
                count -= num
            else:
                count += num
        return count != 0
        
