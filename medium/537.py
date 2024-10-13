class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = num1.split('+')
        r2, i2 = num2.split('+')
        real = str(int(r1) * int(r2) - (int(i1[:len(i1) - 1]) * int(i2[:len(i2) - 1])))
        imag = str(int(r1) * int(i2[:len(i2) - 1]) + int(r2) * int(i1[:len(i1) - 1])) + 'i'
        return f"{real}+{imag}"

