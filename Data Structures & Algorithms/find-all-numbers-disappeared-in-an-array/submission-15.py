class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing.append(i)
        return missing