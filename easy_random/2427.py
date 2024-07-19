class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b:
            factor = a
        else:
            factor = b

        res = 0
        while factor >= 1:
            if a % factor == 0 and b % factor == 0:
                res += 1
            factor -= 1

        return res

