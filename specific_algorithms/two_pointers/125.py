class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while r > 0 and not s[r].isalnum():
                r -= 1
            while l < len(s) - 1 and not s[l].isalnum():
                l += 1
            if s[l].lower() == s[r].lower():
                r -= 1
                l += 1
            elif s[l].isalnum() and s[r].isalnum:
                return False
        return True
