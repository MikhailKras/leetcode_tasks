class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = float('inf'), float('-inf')
        for sal in salary:
            min_sal, max_sal = min(min_sal, sal), max(max_sal, sal)
        return round((sum(salary) - min_sal - max_sal) / (len(salary) - 2), 5)
        
