class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relative=[]
        for i in arr2:
            a=arr1.count(i)
            relative.extend([i]*a)
        remaining=[x for x in arr1 if x not in relative]
        relative.extend(sorted(remaining))
        return relative