class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avgs = []
        nums.sort()
        nums = deque(nums)
        for _ in range(len(nums) // 2):
            avgs.append((nums.popleft() + nums.pop()) / 2)
        return min(avgs)

