class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def helper(arr: List[int], i: int):
            if i == n:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            helper(arr, i + 1)

            arr.pop()
            helper(arr, i + 1)

        helper([], 0)
        return res

