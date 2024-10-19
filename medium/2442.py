class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            reverse_num = int(str(num)[::-1])
            if reverse_num not in seen:
                seen.add(reverse_num)
        return len(seen)

