class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d=0
        j=0
        while d<len(s):
            if s[d] in t[j:]:
                d+=1
                j+=1
            else:
                d+=1
                j+=1
        it=iter(t)
        if all(c in it for c in s):
            return True
        else:
            return False