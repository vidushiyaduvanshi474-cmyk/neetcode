class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=[]
        a=words[0]
        for i in range(0,len(a)):
            if all(a[i] in word for word in words):
                if a[:i+1].count(a[i])<= min(word.count(a[i]) for word in words):
                    common.append(a[i])
        return common