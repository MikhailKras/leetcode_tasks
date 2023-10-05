class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        res1 = 1
        res2 = 0
        for digit in n:
            res1 *= int(digit)
            res2 += int(digit)
        return res1 - res2
