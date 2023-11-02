class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_res, res = 0, 0
        for num in nums:
            if num == 1:
                res += 1
            else:
                max_res = max(res, max_res)
                res = 0
        else:
            max_res = max(res, max_res)
        return max_res

