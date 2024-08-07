class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num: int) -> int:
            str_num = str(num)
            return int(len(str_num) * max(str_num))
        
        res = 0
        for num in nums:
            res += encrypt(num)
        return res

