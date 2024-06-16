class Solution:
    def get_left_and_right_sums(self, nums: List[int], pref_sum: List[int], mid: int) -> Tuple[int]:
        if mid == 0:
            l_sum = 0
            r_sum = pref_sum[-1] - nums[0]
        elif mid == len(nums) - 1:
            l_sum = pref_sum[-1] - nums[-1]
            r_sum = 0
        else:
            l_sum = pref_sum[mid]
            r_sum = pref_sum[-1] - pref_sum[mid + 1]
        return l_sum, r_sum

    def findMiddleIndex(self, nums: List[int]) -> int:
        pref_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(pref_sum)):
            pref_sum[i] = pref_sum[i - 1] + nums[i - 1]
        
        for mid in range(len(nums)):
            l_sum, r_sum = self.get_left_and_right_sums(nums, pref_sum, mid)
            if l_sum == r_sum:
                return mid
        
        return -1

