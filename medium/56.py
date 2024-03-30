class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            first, second = intervals[i], intervals[i + 1]
            if first[0] <= second[0] <= first[1]:
                intervals[i + 1] = [first[0], max(first[1], second[1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals

