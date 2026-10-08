class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            if nums.count(i)>len(nums)/2:
                if a==i:
                    pass
                else:
                    a+=i
        return a
        