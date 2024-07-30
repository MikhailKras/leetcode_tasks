class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                val = 2 * stack.pop() or 1
                stack[-1] += val
        return stack[-1]

