class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed.pop(0)]
        while True:
            try:
                if stack and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    stack.append(pushed.pop(0))
            except Exception:
                break
        return not pushed and not popped

