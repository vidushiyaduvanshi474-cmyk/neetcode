from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        condition=False
        if Counter(s)==Counter(t):
            return True
        else:
            return False

