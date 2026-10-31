from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran=0
        if len(magazine)<len(ransomNote):
            return False
        else:
            if ransomNote in magazine:
                return True
            elif Counter(ransomNote)==Counter(magazine):
                return True
            elif len(ransomNote)<len(magazine):
                h=list(magazine)
                for i in ransomNote:
                    if i in h:
                        h.remove(i)
                        ran+=1
                if ran==len(ransomNote):
                    return True
                else:
                    return False
            else:
                return False
        