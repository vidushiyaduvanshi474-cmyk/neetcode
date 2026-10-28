class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good=[]
        for i in range(0,len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                good.append(int(num[i]))
        if len(good)>=1:
            a=max(good)
            return str(a)*3
        else:
            return ""