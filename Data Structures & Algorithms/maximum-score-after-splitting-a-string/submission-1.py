class Solution:
    def maxScore(self, s: str) -> int:
        a=list(s)
        b=0
        score=[]
        left=""
        right=""
        while b<len(a):
            left+=a.pop(b)
            right+="".join(a)
            if len(left)>0 and len(right)>0:
                score.append((left.count("0")+right.count("1")))
            right=""
        return max(score)