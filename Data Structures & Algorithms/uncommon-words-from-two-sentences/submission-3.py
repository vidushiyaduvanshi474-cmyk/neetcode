class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon=[]
        a=list(s1.split())+(s2.split())
        for i in a:
            if a.count(i)==1:
                uncommon.append(i)
        return uncommon
