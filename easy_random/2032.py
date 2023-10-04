from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1, set2, set3, set_all = set(nums1), set(nums2), set(nums3), set(nums1 + nums2 + nums3)
        res = set()
        for num in set_all:
            if (num in set1 and num in set2) or (num in set1 and num in set3) or (num in set2 and num in set3):
                res.add(num)
        return list(res)
