class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g=0
        gg=0
        while g<=len(nums)-1:
            if nums[g]!=0:
                nums[gg],nums[g]=nums[g],nums[gg]
                gg+=1
            g+=1
        print(nums)


              