class Solution:
    def maxPower(self, s: str) -> int:
        max_val, cur_val, cur = 0, 0, s[0]
        for char in s:
            if char != cur:
                cur = char
                max_val = max(max_val, cur_val)
                cur_val = 0
            cur_val += 1
        return max(max_val, cur_val)
        
