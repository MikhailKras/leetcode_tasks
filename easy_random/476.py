class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num = list(num)
        for i in range(len(num)):
            if num[i] == '0':
                num[i] = '1'
            else:
                num[i] = '0'
        return int(''.join(num), 2)
        
