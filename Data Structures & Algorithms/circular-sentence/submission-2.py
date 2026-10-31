class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        if sentence[0]!=sentence[-1]:
            return False
        elif len(sentence.split())==1:
            if sentence[0]==sentence[-1]:
                return True
            else:
                return False
        else:
            for i in range(0,len(words)-1):
                cur=words[i]
                nex=words[i+1]
                if cur[-1]!=nex[0]:
                    return False
                    break
            return True
