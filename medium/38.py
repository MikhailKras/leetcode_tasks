class Solution:
    def countAndSay(self, n: int) -> str:
        dn = [-1 for _ in range(n + 1)]
        dn[1] = "1"
        for i in range(2, n + 1):
            res, cur, count = "", dn[i - 1][0], 0
            for char in dn[i - 1]:
                if char != cur:
                    res += f"{count}{cur}"
                    cur, count = char, 1
                else:
                    count += 1
            else:
                res += f"{count}{cur}"
            dn[i] = res
        print(dn)
        return dn[n]
            
