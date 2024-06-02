class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefs = [1 for _ in range(len(nums))]
        prefs[0] = nums[0]
        for i in range(1, len(nums)):
            prefs[i] = (prefs[i - 1] or 1) * nums[i]
            
        res = max(prefs)
        index_divider = None
        for i in range(len(prefs)):
            if index_divider is not None:
                res = max(res, prefs[i] // prefs[index_divider])
            if prefs[i] < 0:
                if index_divider is not None:
                    if prefs[i] > prefs[index_divider]:
                        index_divider = i
                else:
                    index_divider = i
            elif prefs[i] == 0:
                index_divider = None

        return max(res, max(nums))

