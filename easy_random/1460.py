class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        seen_target, seen_arr = {}, {}
        for num1, num2 in zip(target, arr):
            seen_target[num1] = seen_target.get(num1, 0) + 1
            seen_arr[num2] = seen_arr.get(num2, 0) + 1
        return seen_target == seen_arr
        
