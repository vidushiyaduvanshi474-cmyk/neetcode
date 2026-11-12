class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values=[]
        repeatandmiss=[]
        for i in grid:
            for j in i:
                values.append(j)
        for m in range(1,len(values)+1):
            if values.count(m)>=2:
                repeatandmiss.append(m)
        for n in range(1,len(values)+1):
            if  n not in values:
                repeatandmiss.append(n)
        return repeatandmiss

        