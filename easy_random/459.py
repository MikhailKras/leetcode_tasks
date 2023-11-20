class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def check_repeat(pat):
            p = len(pat)
            rem = n % p
            if rem:
                return False
            rep = n // p
            return pat * rep == s
        pattern = ''
        for char in s[:n // 2]:
            pattern += char
            if check_repeat(pattern):
                return True
        return False
        
