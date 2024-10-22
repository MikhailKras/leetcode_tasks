class Solution:
    def minimumSum(self, num: int) -> int:
        res = float('inf')
        def helper(cur1, cur2, remains):
            nonlocal res
            if not remains:
                print(cur1, cur2)
                if cur1 and cur2:
                    res = min(res, int(cur1) + int(cur2))
                return
            for i in range(len(remains)):
                helper(cur1 + remains[i], cur2, remains[:i] + remains[i + 1:])
                helper(cur1, cur2 + remains[i], remains[:i] + remains[i + 1:])
        helper('', '', list(str(num)))
        return res

