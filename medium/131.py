class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(cur, part, i):
            if i == len(s):
                if not part:
                    res.append(cur)
                return
            new_part = part + s[i]
            if new_part == new_part[::-1]:
                helper(cur + [new_part], "", i + 1)
            helper(cur, new_part, i + 1)
        
        helper([], "", 0)
        return res
        
