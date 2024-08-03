class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        res = []
        s = s[1:len(s) - 1]
        def helper(i, cur, is_first):

            def make_second():
                if "." not in cur:
                    helper(i + 1, cur + ", " + s[i], False)
                else:
                    if cur[-1] != "0":
                        helper(i + 1, cur + ", " + s[i], False)

            if i == len(s):
                res.append("(" + cur + ")")
                return
            if is_first:
                if i == len(s) - 1:
                    make_second()
                elif i == 0:
                    helper(i + 1, cur + s[i], True)
                elif i == 1 and len(s) > 2:
                    make_second()
                    if cur[-1] != "0":
                        helper(i + 1, cur + s[i], True)
                    helper(i + 1, cur + "." + s[i], True)
                else:
                    make_second()
                    helper(i + 1, cur + s[i], True)
                    if "." not in cur.split(", ")[0]:
                        helper(i + 1, cur + "." + s[i], True)
            else:
                val = cur.split(", ")[-1]
                if "." in val and s[i] == "0" and i + 1 == len(s):
                    return
                if val[0] != "0" or "." in val:
                    helper(i + 1, cur + s[i], False)
                if cur[-3] == "," or "." not in val:
                    if s[i] == "0" and i + 1 == len(s):
                        return
                    helper(i + 1, cur + "." + s[i], False)
        helper(0, "", True)
        return res

