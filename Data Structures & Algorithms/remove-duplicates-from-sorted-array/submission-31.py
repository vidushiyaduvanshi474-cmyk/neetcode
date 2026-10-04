class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d=0
        f=1
        while d<len(nums)-1:
            if nums[d]==nums[f]:
                nums.pop(f)
            else:
                d+=1
                f+=1
        return len(nums)
        