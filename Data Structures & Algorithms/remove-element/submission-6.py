class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        while a<len(nums):
            if nums[a]==val:
                nums.remove(val)
            else:
                a+=1
        return len(nums)