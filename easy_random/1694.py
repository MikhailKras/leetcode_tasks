class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        res, n = [], len(number)
        count = n // 3
        remain = n % 3
        if remain == 1:
            count -= 1
            remain += 3
        
        x = 0
        for i in range(count):
            res.append(number[x:x+3])
            x += 3
        
        if remain in (2, 3):
            res.append(number[n-remain:])
        elif remain == 4:
            res.extend([number[n-remain:n-remain+2], number[n-remain+2:]])
        
        return '-'.join(res)


