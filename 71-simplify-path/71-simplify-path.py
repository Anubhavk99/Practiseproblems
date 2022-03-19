class Solution:
    def simplifyPath(self, path: str) -> str:
        p=['/']
        d=''
        k=[]
        for p in path.split("/"):
            if p == "..":
                if k:
                    k.pop()
            elif p and p != '.':
                k.append(p)
        print(k)
        return '/'+'/'.join(k)