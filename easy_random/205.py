class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transform_dict = {}
        used_t = set()
        for ss, tt in zip(s, t):
            if ss not in transform_dict:
                if tt in used_t:
                    return False
                transform_dict[ss] = tt
                used_t.add(tt)
            else:
                if transform_dict[ss] != tt:
                    return False
        return True

