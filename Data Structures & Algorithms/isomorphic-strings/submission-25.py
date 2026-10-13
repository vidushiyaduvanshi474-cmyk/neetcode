class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=0
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                for j in range(1,len(s)):
                    if s[i]==s[j] and t[i]!=t[j]:
                        return False
                    if s[i]!=s[j] and t[i]==t[j]:
                        return False
            return True
                