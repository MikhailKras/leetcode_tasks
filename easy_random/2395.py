class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(1, len(nums)):
            cur = nums[i - 1] + nums[i]
            if cur in seen:
                return True
            seen.add(cur)
        return False

