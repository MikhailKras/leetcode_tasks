class Solution:
    def splitNum(self, num: int) -> int:
        sort_num = sorted(str(num))
        num1, num2 = '', ''
        for i in range(len(sort_num)):
            if i % 2 == 0:
                num1 += sort_num[i]
            else:
                num2 += sort_num[i]
        return int(num1) + int(num2)

