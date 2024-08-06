class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        values = list(seen.values())
        max_freq = max(values)
        return max_freq * values.count(max_freq)

