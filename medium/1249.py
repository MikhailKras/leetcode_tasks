class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i = 0
        stack = []
        s = list(s)
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    s.pop(i)
                    i -= 1
            i += 1
        count = len(stack)
        j = len(s) - 1
        while count > 0 and j >= 0:
            if s[j] == "(":
                s.pop(j)
                count -= 1
            j -=1

        return ''.join(s)

