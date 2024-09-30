class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        seen_s, seen_t = {}, {}
        for i in range(len(s)):
            seen_s[s[i]] = i
            seen_t[t[i]] = i
        res = 0
        for char in seen_s:
            res += abs(seen_s[char] - seen_t[char])
        return res

