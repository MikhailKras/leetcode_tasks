from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def factorial(num):
            if num == 1:
                return num
            return num * factorial(num - 1)
        
        res = [1]
        for i in range(1, (rowIndex + 2) // 2):
            match i:
                case 1:
                    res.append(rowIndex)
                case 2:
                    res.append(rowIndex * (rowIndex - 1) // 2)
                case _:
                    numerator = factorial(rowIndex)
                    denominator = factorial(i) * factorial(rowIndex - i)
                    res.append(numerator // denominator)
                    
        reflect = res[::-1] if rowIndex % 2 else res[:-1][::-1]
        return res + reflect
        
