class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n0, n1 = 0, 0
        for dig in s:
            if dig == '0':
                n0 += 1
            else:
                n1 += 1
        return (n1 - 1) * '1' + n0 * '0' + '1'

