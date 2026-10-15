class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s=[]
        ss=[]
        for i in range(0,len(nums)-1):
            if nums[i+1]>nums[i]:
                if len(s)==0:
                    s.append(nums[i])
                s.append(nums[i+1])
            else:
                if len(s)==0:
                    ss.append(nums[i])
                else:
                    ss.append(sum(s))
                    s=[]
        ss.append(sum(s))
        return max(max(nums),max(ss))