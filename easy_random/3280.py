class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res = []
        for num in date.split('-'):
            res.append(bin(int(num))[2:])
        return '-'.join(res)
        
