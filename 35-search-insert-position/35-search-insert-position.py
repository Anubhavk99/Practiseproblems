class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        if target==max(nums):
            return len(nums)-1
        elif target>max(nums):
            return len(nums)
        else:
            while nums[i]<=target:
                if nums[i]==target:
                    return i
                    break
                i+=1
        return i
        