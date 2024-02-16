class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return str(num)[-1] != '0'

