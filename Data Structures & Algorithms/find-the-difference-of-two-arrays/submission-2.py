class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[]
        notinnums2=[]
        notinnums1=[]
        for i in nums1:
            if i not in nums2:
                notinnums2.append(i)
        for j in nums2:
            if j not in nums1:
                notinnums1.append(j)
        a=set(notinnums2)
        b=set(notinnums1)
        notinnums2=[x for x in a]
        notinnums1=[y for y in b]
        answer.append(notinnums2)
        answer.append(notinnums1)
        return answer