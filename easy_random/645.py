class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_all = (1 + n) * n // 2
        sum_cur = sum(nums)
        sum_set = sum(set(nums))
        return [sum_cur - sum_set, sum_all - sum_set]

