class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp, sp = 0, 0
        while gp < len(g) and sp < len(s):
            if s[sp] >= g[gp]:
                gp += 1
            sp += 1
        return gp
        
