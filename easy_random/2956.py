class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1, snums2 = set(nums1), set(nums2)
        return [
            len([x for x in nums1 if x in snums2]),
            len([y for y in nums2 if y in snums1])
        ]
        
