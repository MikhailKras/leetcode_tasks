class Solution:
    def largestInteger(self, num: int) -> int:
        odd, even = [], []
        i = 0
        num = list(str(num))
        while i < len(num):
            if int(num[i]) % 2 == 0:
                dig, num[i] = num[i], 'e'
                even.append(dig)
            else:
                dig, num[i] = num[i], 'o'
                odd.append(dig)
            i += 1
        odd.sort(), even.sort()
        for j in range(len(num)):
            if num[j] == 'e':
                num[j] = even.pop()
            else:
                num[j] = odd.pop()
        return int(''.join(num))

