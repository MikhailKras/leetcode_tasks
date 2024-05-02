class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return [0, 0] if target in nums else [-1, -1]

        def right_binsearch() -> int:
            res = -1
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r + 1) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid
                elif nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        res = mid
                        break
                    else:
                        l = mid
            return res
        
        def left_binsearch() -> int:
            res = -1
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        res = mid
                        break
                    else:
                        r = mid
            return res
        
        start, end = left_binsearch(), right_binsearch(),
        
        if end == -1 and start != -1:
            end = start
        elif start == -1 and end != -1:
            start = end
        
        return [start, end]

