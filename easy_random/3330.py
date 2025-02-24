class Solution:
    def possibleStringCount(self, word: str) -> int:
        last = word[0]
        cur = 1
        res = 1
        for i in range(1, len(word)):
            if word[i] == last:
                cur += 1
            else:
                res += cur - 1
                cur = 1
                last = word[i]
        return res + cur - 1

