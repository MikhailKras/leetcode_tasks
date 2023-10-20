class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            str_num = str(num)
            if '0' not in str_num and len(list(filter(lambda x: num % int(x) == 0, str_num))) == len(str_num):
                res.append(num)
        return res

