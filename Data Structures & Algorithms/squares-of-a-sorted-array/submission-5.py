class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nu=[]
        for i in nums:
            nu.append(i**2)
        nu.sort()
        return nu
        