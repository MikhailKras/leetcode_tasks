class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = [], True
        for i in range(0, len(s), k):
            if flag:
                res.append(s[i:i+k][::-1])
                flag = False
            else:
                res.append(s[i:i+k])
                flag = True
        return "".join(res)  

