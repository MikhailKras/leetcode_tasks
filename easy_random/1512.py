class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        res = 0
        for x in seen.values():
            res += x * (x - 1) // 2
        return res

