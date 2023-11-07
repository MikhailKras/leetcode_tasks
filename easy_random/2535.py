class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum, dig_sum = sum(nums), sum(map(int, list(''.join(list(map(str, nums))))))
        return abs(el_sum - dig_sum)

