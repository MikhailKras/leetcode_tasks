class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for num, ind in zip(nums, index):
            res.insert(ind, num)
        return res

