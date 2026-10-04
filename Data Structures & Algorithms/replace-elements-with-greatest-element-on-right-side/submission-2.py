class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g=0
        while g<len(arr):
            if g==len(arr)-1:
                arr[g]=-1
            else:
                f=max(arr[g+1:])
                arr[g]=f
            g+=1
        return arr
        