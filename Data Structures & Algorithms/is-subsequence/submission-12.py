class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it=iter(t)
        if all(c in it for c in s):
            return True
        else:
            return False