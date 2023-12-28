class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = duration
        now = timeSeries[0] + duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] < now:
                res -= timeSeries[i - 1] + duration - timeSeries[i]
            res += duration
            now = timeSeries[i] + duration
        return res
        
