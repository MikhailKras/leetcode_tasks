class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for dig in str(num):
            if num % int(dig) == 0:
                res += 1
        return res
        
