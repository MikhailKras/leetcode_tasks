class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0'*(len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0'*(len(b) - len(a)) + a 
        
        adl = 0
        ac, bc = len(a) - 1, len(b) - 1
        res = ''
        while ac == bc >= 0:
            ai, bi = int(a[ac]), int(b[bc])
            sm = int(a[ac]) + int(b[bc]) + adl
            match sm:
                case 0:
                    res = '0' + res
                    adl = 0
                case 1:
                    res = '1' + res
                    adl = 0
                case 2:
                    res = '0' + res
                    adl = 1
                case 3:
                    res = '1' + res
                    adl = 1
            ac -= 1
            bc -= 1
        return res if adl == 0 else '1' + res
        
