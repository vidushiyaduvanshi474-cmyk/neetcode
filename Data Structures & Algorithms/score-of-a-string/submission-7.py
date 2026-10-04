class Solution:
    def scoreOfString(self, s: str) -> int:
        f=0
        g=1
        cou=0
        while g<len(s):
            if len(s)>0:
                if ord(s[f])>ord(s[g]):
                    cou+=(ord(s[f])-ord(s[g]))
                else:
                    cou+=(ord(s[g])-ord(s[f]))
            f+=1
            g+=1
        return cou
