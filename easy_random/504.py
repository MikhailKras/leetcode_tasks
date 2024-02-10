class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        if num < 0:
            num = -1 * num
            res.append('-')
        while num != 0:
            rem, num = num % 7, num // 7
            print(num)
            res.append(str(rem))
        if res[0] == '-':
            return '-' + ''.join(res[1:][::-1])
        return ''.join(res[::-1])

