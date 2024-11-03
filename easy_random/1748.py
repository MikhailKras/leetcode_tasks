class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        return sum([num for num in seen if seen[num] == 1])

