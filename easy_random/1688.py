class Solution:
    def numberOfMatches(self, n: int) -> int:
        def helper(res, teams):
            if teams == 1:
                return res
            return helper(res + teams // 2, (teams + 1) // 2)
        
        return helper(0, n)

