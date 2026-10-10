class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        y=0
        t=sorted(heights)
        for i in range(0,len(heights)):
            if heights[i]!=t[i]:
                y+=1
        return y