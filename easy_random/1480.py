class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n, res = 0, []
        for num in nums:
            n += num
            res.append(n)
        return res

