class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        return all(True if cnt % 2 == 0 else False for cnt in seen.values())
        
