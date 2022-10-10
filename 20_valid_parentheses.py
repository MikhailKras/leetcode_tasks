class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        stack = []
        
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


x = Solution()
print(x.isValid('([)]'))
        