class Solution:
    def longestPalindrome(self, s: str) -> int:
        sum=0
        cc={}
        for i in range(0,len(s)):
            k=s[i]
            cc[s[i]]=s.count(s[i])
        for c in cc.values():
            if c%2!=0:
                sum+=c-1
            else:
                sum+=c
        for i in cc.values():
            print(i)
            if i%2!=0:
                sum+=1
                break
        return sum
        