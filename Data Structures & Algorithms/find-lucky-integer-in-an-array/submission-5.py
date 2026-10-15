class Solution:
    def findLucky(self, arr: List[int]) -> int:
        g=[]
        for i in set(arr):
            if arr.count(i)==i:
                g.append(i)
        if len(g)==0:
            return -1
        else:
            return max(g)