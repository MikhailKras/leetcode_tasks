class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if '-' in x:
            x = '-' + x.replace('-', '')
        x = int(x)
        if x < -2 ** 31 or x > 2 ** 31 -1:
            return 0
        return x