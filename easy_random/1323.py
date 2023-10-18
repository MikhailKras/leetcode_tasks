class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0
        num = str(num)
        while i < len(num) and num[i] != '6':
            i += 1
        else:
            if i == len(num):
                return int(num)
            else:
                return int(num[:i] + '9' + num[i + 1:])

