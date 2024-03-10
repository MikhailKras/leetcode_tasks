class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        res = ''
        for i in range(0, len(s), k):
            res += str(sum(map(int, list(s[i:i+k]))))
        return self.digitSum(res, k)

