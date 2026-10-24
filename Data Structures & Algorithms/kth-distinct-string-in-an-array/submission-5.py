class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr)==len(set(arr)):
            return arr[k-1]
        else:
            uni=[]
            for i in arr:
                if arr.count(i)>=2:
                    pass
                else:
                    uni.append(i)
        if len(uni)>=k:
            return uni[k-1]
        else:
            return ""