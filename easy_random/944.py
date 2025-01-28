class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [list(x) for x in strs]
        res = 0
        for col in zip(*strs):
            if col != tuple(sorted(col)):
                res += 1
        return res

