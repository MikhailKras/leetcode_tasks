class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            left = nums[mid - 1] if mid - 1 >= 0 else nums[mid]
            right = nums[mid + 1] if mid + 1 < n else nums[mid]
            if left <= nums[mid] >= right:
                return mid
            if nums[mid] <= right:
                l = mid + 1
            elif nums[mid] <= left:
                r = mid

