class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        st = set(nums)
        return sorted(st, reverse=True)[2] if len(st) >= 3 else max(st)

