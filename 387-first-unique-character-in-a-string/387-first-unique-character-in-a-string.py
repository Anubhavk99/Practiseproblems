class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=[]
        p=[]
        m=0
        for i in range(0,len(s)):
            if s[i] not in st:
                st.append(s[i])
                p.append(i)
                print(st,p)

            elif s[i] in st:
                k=st.index(s[i])
                p[k]='nil'
            else:
                pass
        print(st,p)
        for j in range(0,len(p)):
                if p[j]=='nil':
                    m+=1
                    pass 
                else:
                    return p[j]
                    break
        if m==len(p):
            return -1
            
        