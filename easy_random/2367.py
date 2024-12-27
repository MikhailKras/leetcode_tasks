class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        l, r = 0, 1
        l_seen, r_seen = set(), set()
        while r < len(nums):
            if nums[r] - nums[l] == diff:
                l_seen.add(l)
                r_seen.add(r)
                l += 1
                r += 1
            elif nums[r] - nums[l] > diff:
                l += 1
            else:
                r += 1
        
        count = 0
        for l in l_seen:
            if l in r_seen:
                count += 1

        return count

