class Solution:
    def firstUniqChar(self, s: str) -> int:
        ind=[]
        for i in range(0,len(s)):
            if s.count(s[i])==1:
                ind.append(i)
        if len(ind)==0:
            return -1
        else:
            return ind[0]
                