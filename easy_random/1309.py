class Solution:
    def freqAlphabets(self, s: str) -> str:
        diff = 96
        res = deque([])
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                res.appendleft(chr(int(s[i-2:i]) + diff))
                i -= 3
            else:
                res.appendleft(chr(int(s[i]) + diff))
                i -= 1
        return "".join(res)

