class Solution:
    def reformat(self, s: str) -> str:
        res = ""
        queue_dig = deque()
        queue_let = deque()
        for char in s:
            if char.isalpha():
                if queue_dig:
                    res += char + queue_dig.popleft()
                else:
                    queue_let.append(char)
            elif char.isdigit():
                if queue_let:
                    res += queue_let.popleft() + char
                else:
                    queue_dig.append(char)
        else:
            if len(queue_dig) == 1:
                res = queue_dig.popleft() + res
            elif len(queue_let) == 1:
                res += queue_let.popleft()
        return "" if queue_dig or queue_let else res

