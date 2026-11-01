class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    common.append(j)
        h=set(common)
        common=[i for i in h]
        return common