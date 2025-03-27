class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x, y = float('-inf'), float('inf')
        for num in nums:
            x, y = max(x, num), min(y, num)

        while y != 0:
            temp, x = x % y, y
            y = temp 
        return x

