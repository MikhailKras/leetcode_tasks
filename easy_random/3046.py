class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > 2:
                return False
        return True
        
