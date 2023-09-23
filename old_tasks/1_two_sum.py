class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_sort = sorted(nums)
        high = len(nums_sort) - 1
        for num1 in nums_sort:
            low = nums_sort.index(num1) + 1
            while low <= high:
                mid = round((low + high) / 2)
                num2 = nums_sort[mid]
                if num1 + num2 == target:
                    if num1 == num2:
                        return [nums.index(num1), nums.index(num2, nums.index(num1) + 1)]
                    else:
                        return [nums.index(num1), nums.index(num2)]
                elif num1 + num2 > target:
                    high = mid - 1
                else:
                    low = mid + 1
