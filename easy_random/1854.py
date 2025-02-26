class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = {year: 0 for year, _ in logs}
        for log in logs:
            b, d = log
            for year in years:
                if b <= year < d:
                    years[year] += 1
        return max(years, key=lambda x: (years[x], -x))

