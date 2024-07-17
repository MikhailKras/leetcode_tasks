class Solution:
    def bin_search(self, arr, target):
        if arr:
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l if arr[l] == target else -1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        if nums[0] < nums[-1]:
            init_index = 0
        else:
            l, r = 1, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[mid - 1]:
                    init_index = mid
                    break
                else:
                    if nums[mid] < nums[0]:
                        r = mid
                    else:
                        l = mid + 1
            else:
                init_index = l

        res = self.bin_search(nums[:init_index], target)
        if res != -1:
            return res
        
        res = self.bin_search(nums[init_index:], target)
        return init_index + res if res != -1 else res

