class Solution(object):
    def decodeString(self, s):
        stack, cur_num, cur_string = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                cur_string = prevString + num * cur_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_string += c
        return cur_string


my_str = "3[a2[c]]"
x = Solution()
print(x.decodeString(my_str))
