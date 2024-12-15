class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        part = n // 20
        arr.sort()
        return sum(arr[part:n - part]) / (n - 2 * part)

