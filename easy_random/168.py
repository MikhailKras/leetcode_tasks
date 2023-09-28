class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ''
        while n > 0:
            n -= 1
            rem = n % 26
            print(rem)
            res = f'{chr(65 + rem)}' + res
            n //= 26
        return res
        
