class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        yy=[]
        for i in words:
            for j in words:
                if j in i:
                    if len(j)<len(i) and j not in yy:
                        yy.append(j)
        return yy