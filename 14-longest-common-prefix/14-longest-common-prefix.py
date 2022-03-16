class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rtn=''
        lenstrs=[]
        t=len(strs)
        fe=strs[0]
        for i in range(0,t):
            lenstrs.append(len(strs[i]))
        minm=min(lenstrs)
        for j in range(0,minm):
            c=0
            for k in range(1,t):
                if fe[j]==strs[k][j]:
                    c+=1
            if c==t-1:
                rtn+=fe[j]
            else:
                break
        return rtn
        