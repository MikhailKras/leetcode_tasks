class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for type_, color, name in items:
            dct = {"type": type_, "color": color, "name": name}
            if dct.get(ruleKey) == ruleValue:
                res += 1
        return res
        
