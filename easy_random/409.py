class Solution:
    def longestPalindrome(self, s: str) -> int:
        res, counter = 0, {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        is_plus_odd = False
        for char in counter:
            if not is_plus_odd:
                if counter[char] % 2 == 1:
                    is_plus_odd = True
                res += counter[char]
            else:
                res += (counter[char] // 2) * 2
        return res

