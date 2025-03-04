class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots = [pivot for _ in range(nums.count(pivot))]
        
        l, r = [], []
        for num in nums:
            if num > pivot:
                r.append(num)
            elif num < pivot:
                l.append(num)
        
        return l + pivots + r

