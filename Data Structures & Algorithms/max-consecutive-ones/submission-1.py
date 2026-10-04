class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cou=0
        ma=0
        for i in nums:
            if i==i==1:
                cou+=1
            else:
                cou=0
            if cou>ma:
                ma=cou
        return ma
        