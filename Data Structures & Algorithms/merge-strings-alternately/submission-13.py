class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        min_len = min(len(word1), len(word2))
        s=""
        while l < min_len:
            s+=word1[l]
            s+=word2[l]
            l+=1
        s += word1[l:]
        s += word2[l:]
        return s
