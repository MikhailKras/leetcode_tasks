class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        while nums:
            arr.extend([nums.pop(1), nums.pop(0)])
        return arr
        
