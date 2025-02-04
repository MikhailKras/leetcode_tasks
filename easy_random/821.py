class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        poses = []
        for i in range(len(s)):
            if s[i] == c:
                poses.append(i)
        
        if len(poses) > 1:
            res = []
            cur = [poses[0], poses[1]]
            j = 2
            for i in range(len(s)):
                res.append(min(abs(i - cur[0]), abs(i - cur[1])))
                if i == cur[1]:
                    cur[0] = cur[1]
                    if j < len(poses):
                        cur[1] = poses[j]
                        j += 1
            return res
        else:
            return [abs(x - poses[0]) for x in range(len(s))]

