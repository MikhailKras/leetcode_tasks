class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        str_n = str(n)
        for i in range(len(str_n)):
            if i % 2 == 0:
                res += int(str_n[i])
            else:
                res -= int(str_n[i])
        return res

