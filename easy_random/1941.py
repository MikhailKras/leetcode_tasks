class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        return len(set(seen.values())) == 1

