class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {char: val for val, char in enumerate(order)}
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
            
        res = ""
        for char in order_dict:
            if char in seen:
                res += seen[char] * char
        
        for char in seen:
            if char not in order_dict:
                res += seen[char] * char
        
        return res

