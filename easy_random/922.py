class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev, od, n = 0, 1, len(nums)
        while not (ev == n - 2 and od == n - 1):
            if nums[ev] % 2 == 0:
                if ev + 2 != n:
                    ev += 2
            if nums[od] % 2 == 1:
                if od + 2 != n + 1:
                    od += 2
            if nums[ev] % 2 == 1 and nums[od] % 2 == 0:
                nums[ev], nums[od] = nums[od], nums[ev]
        if nums[-2] % 2 == 1 and nums[-1] % 2 == 0:
            nums[ev], nums[od] = nums[od], nums[ev]
        return nums
            
