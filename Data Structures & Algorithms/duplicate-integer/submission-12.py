class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cou=0
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                cou+=1
        if cou>=1:
            return True
        else:
            return False