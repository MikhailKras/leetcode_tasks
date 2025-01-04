class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        center = ""
        if n % 2 == 0:
            first, second = s[:n//2], s[n//2:]
        else:
            first, second = s[:n//2], s[n//2+1:]
            center = s[n//2]
        if first == second[::-1]:
            return s
        new_first, new_second = "", ""
        for f, s in zip(first, second[::-1]):
            if f != s:
                if ord(f) > ord(s):
                    f = s
                else:
                    s = f
            new_first += f
            new_second += s
        return new_first + center + new_second[::-1]

