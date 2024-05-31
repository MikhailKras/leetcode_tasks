class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        def binary_to_decimal(binary):
            decimal, i = 0, 0
            while binary != 0:
                dec = binary % 10
                decimal = decimal + dec * 2 ** i
                binary = binary // 10
                i += 1
            return decimal
        for i in range(binary_to_decimal(int('1' * n)) + 1):
            check_bin = bin(i)[2:]
            check_bin = (n - len(check_bin)) * '0' + check_bin
            if check_bin not in nums:
                return check_bin

