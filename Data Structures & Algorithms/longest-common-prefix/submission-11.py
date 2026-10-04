class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        while i<len(strs[0]):
            if all(i<len(word) and word[i]==strs[0][i] for word in strs):
                i+=1
            else:
                break
        pre=strs[0][:i]
        return pre