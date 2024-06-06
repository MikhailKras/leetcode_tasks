class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        res = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for key, value in counter.items():
            if counter[key] > freq:
                res.append(key)
        return res

