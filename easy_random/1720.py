class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        cur = first
        for num in encoded:
            next_arr = cur ^ num
            res.append(next_arr)
            cur = next_arr
        return res
        
