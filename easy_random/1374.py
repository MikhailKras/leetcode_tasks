class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        if n % 2 == 0:
            return 'a' + (n - 1) * 'b'
        else:
            return 'a' + 'b' + (n - 2) * 'c'
         
