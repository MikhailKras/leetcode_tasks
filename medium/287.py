class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for key, val in seen.items():
            if val > 1:
                return key

