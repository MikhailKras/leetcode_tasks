class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(cur, remains):
            if remains == []:
               res.append(cur)
               return

            for i in range(len(remains)):
                if not (i > 0 and remains[i] == remains[i - 1]):
                    helper(cur + [remains[i]], remains[:i] + remains[i + 1:])

        helper([], sorted(nums))
        return res

