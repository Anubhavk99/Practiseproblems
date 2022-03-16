class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=0
        i=len(s)-1
        if ord(s[-1])!=32:
            while i>=0:
                if ord(s[i])==32:
                    break
                k+=1
                i-=1
        else:
            while ord(s[i])==32:
                i-=1
            while i>=0:
                if ord(s[i])==32:
                    break
                k+=1
                i-=1
        return k