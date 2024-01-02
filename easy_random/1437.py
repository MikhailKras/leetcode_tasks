class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        last_one = nums.index(1)
        for i in range(last_one + 1, len(nums)):
            if nums[i] == 1:
                if i - last_one - 1 < k:
                    return False
                last_one = i
        return True

