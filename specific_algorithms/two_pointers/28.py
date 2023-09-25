class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                right, j = i, 0
                while right < len(haystack) and haystack[right] == needle[j]:
                        if j == len(needle) - 1:
                            return i
                        j += 1
                        right += 1
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        left = 0
        if haystack == needle:
            return 0
        for right in range(len(needle), len(haystack) + 1):
            if haystack[left:right] == needle:
                return left
            left += 1
        return -1
