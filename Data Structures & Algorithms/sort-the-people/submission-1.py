class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        out=[]
        y=sorted(heights,reverse=True)
        if len(names)!=len(heights):
            return []
        else:
            for i in range(0,len(y)):
                yy=heights.index(y[i])
                out.append(names[yy])
        if len(out)==len(names):
            return out
        else:
            return []        
