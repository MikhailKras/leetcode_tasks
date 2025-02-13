class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank != 0:
            print(mainTank)
            if mainTank >= 5:
                mainTank -= 5
                res += 50
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                res += mainTank * 10
                mainTank -= mainTank
        return res
        
