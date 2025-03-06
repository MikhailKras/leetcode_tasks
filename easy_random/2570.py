class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        while nums1 and nums2:
            if nums1[0][0] == nums2[0][0]:
                res.append([nums1[0][0], nums1.pop(0)[1] + nums2.pop(0)[1]])
            elif nums1[0][0] > nums2[0][0]:
                res.append([nums2[0][0], nums2.pop(0)[1]])
            else:
                res.append([nums1[0][0], nums1.pop(0)[1]])

        if nums1:
            res += nums1
        else:
            res += nums2
        
        return res

