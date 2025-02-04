class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        
        seen = set()
        for count in counter.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True
        
