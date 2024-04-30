class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        nums = list(range(1, n + 1))
        i, j, res = 0, 0, []
        while i < len(target):
            res.append('Push')
            if nums[j] == target[i]:
                i += 1
            else:
                res.append('Pop')
            j += 1
        return res

