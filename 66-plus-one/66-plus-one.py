class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in range(0,len(digits)):
            s+=str(digits[i])
        print(s)
        s=int(s)
        s+=1
        digits=list(str(s))
        return digits
                    