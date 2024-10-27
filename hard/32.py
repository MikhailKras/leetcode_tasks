class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cur = 0
        stack = deque([-1])
        for i in range(len(s)):
            if s[i] == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    cur = max(cur, i - stack[-1])
            else:
                stack.append(i)
        return cur

