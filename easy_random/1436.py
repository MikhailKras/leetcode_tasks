class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, ends = set(), set()
        for start, end in paths:
            starts.add(start)
            ends.add(end)
        for end in ends:
            if end not in starts:
                return end

