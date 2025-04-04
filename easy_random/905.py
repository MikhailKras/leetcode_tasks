class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] % 2 == 1:
                l -= 1
            elif nums[r] % 2 == 0:
                r += 1
            l += 1
            r -= 1
        return nums
        
