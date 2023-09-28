class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            m = (left + right + 1) // 2
            if m * m <= x:
                left = m
            else:
                right = m - 1
        return left
        
