class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float('inf')
        for num in nums:
            min_val = min(min_val, sum(map(int, str(num))))
        return min_val

