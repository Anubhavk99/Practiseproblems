class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = []
        lngst = 0
        for letter in s:
            if letter in c:
                idx = c.index(letter)
                del c[0:idx+1]
            c.append(letter)
            lngst = max(lngst,len(c))
        return(lngst)
        