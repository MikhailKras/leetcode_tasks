class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        set_nums = set(nums)
        for i in range(1, n + 1):
            if i not in set_nums:
                res.append(i)
        return res

