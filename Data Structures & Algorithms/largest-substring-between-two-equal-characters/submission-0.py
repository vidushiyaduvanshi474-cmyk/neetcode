class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        equal=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    equal.append((j-i)-1)
        if len(equal)>0:
            return max(equal)
        else:
            return -1