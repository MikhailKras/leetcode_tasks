class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
                cur_depth += 1
                max_depth = max(cur_depth, max_depth)
            elif char == ")":
                stack.pop()
                cur_depth -= 1
        return max_depth

