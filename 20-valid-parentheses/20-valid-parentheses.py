class Solution:
    def isValid(self, s: str) -> bool:
        k=0
        ob=[]
        if len(s)%2!=0:
            return False
        else:
            for i in range(0,len(s)):  
               if ord(s[i])==40 or ord(s[i])==91 or ord(s[i])==123:
                  ob.append(s[i])
               if ord(s[i])==41 or ord(s[i])==93 or ord(s[i])==125:
                 if len(ob)>0:
                    if ord(s[i])==ord(ob[-1])+1 or ord(s[i])==ord(ob[-1])+2:
                        ob.pop()
                    else:
                        return False
                        break
                 else:
                        return False
                        break
            if len(ob)==0:
                 return True
            

            
        