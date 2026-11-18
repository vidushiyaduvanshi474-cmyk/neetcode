class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k  and i!=j:
                    return True
                    break
        return False