class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        n = len(s)
        len_first = n % k
        if len_first >= len(s):
            return s.upper()
        res = s[:len_first].upper() + '-' if len_first > 0 else ''
        cur_len = 0
        for char in s[len_first:]:
            res += char.upper()
            cur_len += 1
            if cur_len == k:
                res += '-'
                cur_len = 0
        return res if res[-1] != '-' else res[:-1]
        
