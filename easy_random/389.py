class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s, dict_t = {}, {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        for char in dict_t:
            if char not in dict_s or dict_t[char] != dict_s[char]:
                return char
        
