class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rs, ls, res = 0, 0, 0
        for c in s:
            if c == 'R':
                rs += 1
            elif c == 'L':
                ls += 1
            if rs == ls:
                res += 1
                rs, ls = 0, 0
        return res

