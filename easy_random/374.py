# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            pick = guess(m)
            if pick == 0:
                return m
            elif pick == -1:
                r = m
            else:
                l = m + 1
        return l
        
