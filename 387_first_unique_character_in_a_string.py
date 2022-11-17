class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for i in range(len(s)):
            dct[s[i]] = dct.get(s[i], 0) + 1
        for i in range(len(s)):
            if dct[s[i]] == 1:
                return i
        return -1