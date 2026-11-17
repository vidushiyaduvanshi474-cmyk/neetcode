class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss_dup=[]
        for i in set(nums):
            if nums.count(i)>=2:
                miss_dup.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                miss_dup.append(i)
        return miss_dup