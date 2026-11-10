class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        assign=0
        for i in sorted(g):
            for j in sorted(s[:]):
                if j>=i:
                    assign+=1
                    s.remove(j)
                    break
        return assign