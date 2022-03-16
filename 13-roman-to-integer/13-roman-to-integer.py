class Solution:
    def romanToInt(self, s: str) -> int:
        k=0
        for i in range(0,len(s)):
             if s[i]=='I':
                if i!=len(s)-1:
                    if s[i+1]=='V':
                         k-=1
                    elif s[i+1]=='X':
                         k-=1
                    else:
                         k+=1
                else:
                    k+=1
             elif s[i]=='V':
                k+=5
             elif s[i]=='X':
                if i!=len(s)-1:
                    if s[i+1]=='L':
                         k-=10
                    elif s[i+1]=='C':
                         k-=10
                    else:
                         k+=10
                else:
                    k+=10
             elif s[i]=='L':
                k+=50
             elif s[i]=='C':
                if i!=len(s)-1:
                     if s[i+1]=='D':
                        k-=100
                     elif s[i+1]=='M':
                        k-=100
                     else:
                        k+=100
                else:
                    k+=100
             elif s[i]=='D':
                k+=500
             elif s[i]=='M':
                k+=1000
             else:
                pass
        return k
    
     