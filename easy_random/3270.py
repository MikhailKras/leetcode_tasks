class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = []
        for num in (num1, num2, num3):
            num = str(num)
            if len(num) < 4:
                num = "0" * (4 - len(num)) + num
            nums.append(num)
        
        key = ""
        for digits in zip(*nums):
            key += min(digits)
        return int(key)

