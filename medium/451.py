class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        
        res = []
        for char, freq in sorted(seen.items(), key=lambda x: x[1], reverse=True):
            res.extend([char] * freq)
        return ''.join(res)

