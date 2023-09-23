from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        n = len(first_word)

        def check(x):
            pref = first_word[:x]
            for word in strs[1:]:
                if not word.startswith(pref):
                    return False
            return True

        first_word = strs[0]
        n = len(first_word)
        left, right = 0, n
        while left < right:
            m = (left + right + 1) // 2
            if check(m):
                left = m
            else:
                right = m - 1
        return first_word[:left]
