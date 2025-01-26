class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        pairs, leftover = 0, 0
        for count in seen.values():
            pairs += count // 2
            leftover += count % 2
        
        return [pairs, leftover]
        
