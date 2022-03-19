class Solution:
    def simplifyPath(self, path: str) -> str:
        p=['/']
        d=''
        k=''
        for i in range(1,len(path)-1):
                 k = []
        for p in path.split("/"):
            if p == "..":
                if k:
                    k.pop()
            elif p and p != '.':
                k.append(p)
        return '/' + '/'.join(k)