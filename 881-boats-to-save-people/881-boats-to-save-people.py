class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        k=0
        if len(people)%2!=0 and len(people)>1:
            while i<j:
                if people[i]+people[j]<=limit:
                    k+=1
                    i+=1
                    j+=-1
                else:
                    # if j-1<=i:  
                        #k+=2
                       # j+=-1
                     #else:
                        k+=1
                        j+=-1
                        
            if i==j:
                return k+1
            else:
                return k
        elif len(people)%2!=0 and len(people)==1:
            return 1
            
        else:
            while i<j:
                if people[i]+people[j]<=limit:
                    k+=1
                    i+=1
                    j+=-1
                else:
                    #if j-1<=i:  
                        #k+=1
                        #j+=-1
                    #else:
                        k+=1
                        j+=-1
            if i==j:
                return k+1
            else:
                return k
            
            