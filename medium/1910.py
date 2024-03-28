class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        init_index = s.find(part)
        while init_index != -1:
            s = s[:init_index] + s[init_index + n:]
            init_index = s.find(part)
        return s

