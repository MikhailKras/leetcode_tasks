from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = {}, {}
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1

        res = []
        for num in dict1:
            res.extend([num for _ in range(min(dict1[num], dict2.get(num, 0)))])
        return res
