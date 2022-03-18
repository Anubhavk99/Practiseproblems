class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            y=list(str(x))
            y.reverse()
            k=''
            for i in y:
                k+=i
            if int(k)<(2**31)-1:
                return int(k)
            else:
                return 0
        if x<0:
            m=list(str(x))
            y=m[1:len(m)+1]
            y.reverse()
            k=''
            for i in y:
                k+=i
            if int(k)<(2**31)-1:
                l='-'+k
                return int(l) 
            else:
                return 0
        if x==0:
            return 0
            
        
        