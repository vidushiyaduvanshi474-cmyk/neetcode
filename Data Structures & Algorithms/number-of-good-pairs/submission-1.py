class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    good.append([i,j])
        return len(good)