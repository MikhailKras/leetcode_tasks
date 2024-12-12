class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        diff = 0
        for perc in batteryPercentages:
            if perc + diff > 0:
                diff -= 1
                count += 1
        return count

