class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            res = 0
            while num > 0:
                rem = num % 10
                res += rem * rem
                num //= 10
            return res

        left, right = n, n
        while True:
            left = sum_of_squares(left)
            right = sum_of_squares(sum_of_squares(right))
            if left == right:
                break

        return left == 1
