class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        cur = ord('a')
        for char in word:
            left = (ord(char) - cur) % 26
            right = (cur - ord(char)) % 26
            res += min(left, right)
            cur = ord(char)
        return res + len(word)

