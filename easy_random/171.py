class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = columnTitle
        res = 0
        deg, pointer = 0, len(s) -1
        while pointer >= 0:
            res += (ord(s[pointer]) + 1 - 65) * 26 ** deg
            deg += 1
            pointer -= 1
        return res

