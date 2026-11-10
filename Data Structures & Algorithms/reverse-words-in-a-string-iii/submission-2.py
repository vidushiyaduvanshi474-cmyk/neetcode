class Solution:
    def reverseWords(self, s: str) -> str:
        letter=list(s.split())
        reverse=""
        for i in range(0,len(letter)):
            a=letter[i]
            if i==len(letter)-1:
                reverse+=a[::-1]
            else:
                reverse+=a[::-1]+" "
        return reverse
