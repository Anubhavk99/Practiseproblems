class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        k=0
        for i in range(0,ceil(len(x)/2)):
            if x[i]==x[(i+1)*-1]:
                k+=1
        if k==ceil(len(x)/2):
            return True
        else:
            return False