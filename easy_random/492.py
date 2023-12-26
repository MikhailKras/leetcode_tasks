class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** (1/2))
        while area % W != 0:
            W -= 1
        return [area // W, W]

