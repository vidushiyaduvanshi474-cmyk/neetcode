class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(set(nums))==len(nums):
            return False
        elif len(nums)%2==0:
            for i in nums:
                if nums.count(i)%2!=0:
                    return False
                    break
            return True
        else:
            return False
