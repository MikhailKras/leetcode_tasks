class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, n = [], len(s)

        def helper(cur_arr, i):
            if len(cur_arr) == 4 and i > n - 1:
                res.append('.'.join(cur_arr))
                return
            num = ''
            for j in range(i, n):
                num += s[j]
                if int(num) < 256 and not (num.startswith('0') and len(num) > 1): 
                    helper(cur_arr + [num], j + 1)

        helper([], 0)
        return res
        
