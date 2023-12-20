class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        i, n, res, start = 1, len(nums), [], nums[0]
        while i < n:
            if nums[i] - 1 != nums[i - 1]:
                item = f"{start}->{nums[i - 1]}" if nums[i - 1] != start else str(start)
                res.append(item)
                start = nums[i]
            i += 1
        else:
            item = f"{start}->{nums[i - 1]}" if nums[i - 1] != start else str(start)
            res.append(item)
        return res

