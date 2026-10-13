class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                g=j+1
                if nums1[i]==nums2[j]:
                    if g<len(nums2):
                        if nums2[g]>nums2[j]:
                            r.append(nums2[g])
                        elif g+1<len(nums2):
                            for gg in range(g+1,len(nums2)):
                                if nums2[gg]>nums2[j]:
                                    r.append(nums2[gg])
                        else:
                            r.append(-1)
                    else:
                        r.append(-1)
        return r