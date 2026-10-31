class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
       f=sorted(nums)
       a=max(f)
       aa=min(f)
       f.remove(a)
       f.remove(aa)
       b=max(f)
       bb=min(f)
       return ((a*b)-(aa*bb)) 