class Solution:
    def __init__(self):
        self.DICT_ROMAN = {'I': {'value': 1, 'subtraction': ['V', 'X']},
                           'V': {'value': 5, 'subtraction': []},
                           'X': {'value': 10, 'subtraction': ['L', 'C']},
                           'L': {'value': 50, 'subtraction': []},
                           'C': {'value': 100, 'subtraction': ['D', 'M']},
                           'D': {'value': 500, 'subtraction': []},
                           'M': {'value': 1000, 'subtraction': []}}

    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i != 0 and s[i] in self.DICT_ROMAN[s[i - 1]]['subtraction']:
                continue

            if i < len(s) - 1 and s[i + 1] in self.DICT_ROMAN[s[i]]['subtraction']:
                res += (self.DICT_ROMAN[s[i + 1]]['value'] - self.DICT_ROMAN[s[i]]['value'])
            else:
                res += self.DICT_ROMAN[s[i]]['value']

        return res
