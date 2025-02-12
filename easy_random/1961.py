class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        cur = ""
        for word in words:
            cur += word
            if cur == s:
                return True
        return False
        
