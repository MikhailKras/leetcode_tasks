class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = [i for i in range(len(boxes)) if boxes[i] == "1"]
        res = [0 for _ in range(len(boxes))]
        for j in range(len(res)):
            res[j] += sum([abs(i - j) for i in balls])
        return res
