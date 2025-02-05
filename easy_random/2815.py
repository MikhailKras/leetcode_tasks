class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            dmax = max(str(num))
            if dmax in seen:
                seen[dmax].append(num)
            else:
                seen[dmax] = [num]
        
        res = -1
        for arr in seen.values():
            if len(arr) > 1:
                arr.sort(reverse=True)
                res = max(res, arr[0] + arr[1])
        
        return res

