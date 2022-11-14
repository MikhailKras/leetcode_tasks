class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dct = {}
        n = len(nums)
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct.get(num, 0) > n / 2:
                return num
