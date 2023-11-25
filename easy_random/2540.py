class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        inset = set1.intersection(set2)
        return min(inset) if inset else -1
        
