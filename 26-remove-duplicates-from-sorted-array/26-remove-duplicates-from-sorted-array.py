class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            j=i+1
            if nums[i]==nums[j]:
                nums.pop(j)
            else:
                i+=1
        if len(nums)>1:
            return len(nums)
        else:
            return len(nums)
        