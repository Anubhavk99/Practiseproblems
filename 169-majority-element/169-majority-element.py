class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ic={}
        nums.sort()
        c=1
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                c+=1
            else:
                ic[nums[i]]=c
                c=1
        ic[nums[-1]]=c
        for i,j in ic.items():
            if j>floor(len(nums)/2):
                return i
                break
            
        