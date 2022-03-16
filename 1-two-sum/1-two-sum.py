class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newnums = nums.copy()
        while(True):
            n = newnums[0]
            newnums.remove(n)
            for i in newnums:
                if n + i == target:
                    a = nums.index(n)
                    nums.remove(n)
                    b = nums.index(i)+1
                    return [a,b]