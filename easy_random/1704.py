class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        a, b = s[:n // 2], s[n // 2:]
        ca, cb = 0, 0
        for c1, c2 in zip(a, b):
            if c1.lower() in vowels:
                ca += 1
            if c2.lower() in vowels:
                cb += 1
        return ca == cb
        
