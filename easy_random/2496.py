class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_len = 0
        for item in strs:
            for char in item:
                if char.isalpha():
                    max_len = max(max_len, len(item))
                    break
            else:
                max_len = max(max_len, int(item))
        return max_len
        
