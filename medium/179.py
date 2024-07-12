class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def is_greater(x, y):
            x, y = str(x), str(y)
            return x + y > y + x
            

        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            L = merge_sort(arr[:len(arr)//2])
            R = merge_sort(arr[len(arr)//2:])
            res = []
            while L or R:
                if not L:
                    res.append(R.pop(0))
                elif not R:
                    res.append(L.pop(0))
                else:
                    if is_greater(L[0], R[0]):
                        res.append(L.pop(0))
                    else:
                        res.append(R.pop(0))
            return res
        return str(int(''.join(map(str, merge_sort(nums)))))
        
