class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digits_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res, n = [], len(digits)
        
        def helper(cur, i):
            if len(cur) == n:
                res.append(cur)
                return
            for letter in digits_dict[digits[i]]:
                helper(cur + letter, i + 1)
        
        helper('', 0)
        return res

