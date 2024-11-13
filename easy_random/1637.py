class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = [item[0] for item in points]
        x_points.sort()
        res = 0
        for i in range(1, len(x_points)):
            res = max(res, x_points[i] - x_points[i - 1])
        return res
        
