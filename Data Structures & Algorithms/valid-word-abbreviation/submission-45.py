class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        s=0
        ss=0
        while ss<len(abbr):
            if abbr[ss].isalpha():
                if s>=len(word) or abbr[ss]!=word[s]:
                    return False
                    break
                s+=1
                ss+=1
            elif abbr[ss].isdigit():
                if ss+1<len(abbr) and abbr[ss+1].isdigit():
                    p=int(abbr[ss])*10+int(abbr[ss+1])
                    s+=p
                    ss+=2
                else:
                    p=int(abbr[ss])
                    s+=p
                    ss+=1
        if s==len(word) and ss==len(abbr):
            return True
        else:
            return False
