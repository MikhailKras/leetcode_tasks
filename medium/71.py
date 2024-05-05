class Solution:
    def simplifyPath(self, path: str) -> str:
        while '//' in path:
            path = path.replace('//', '/')

        dirs = [x for x in path.split('/') if x]

        res = []
        for dir in dirs:
            match dir:
                case '.':
                    pass
                case '..':
                    if res:
                        res.pop()
                case other:
                    res.append(dir)
        return "/" + "/".join(res)

