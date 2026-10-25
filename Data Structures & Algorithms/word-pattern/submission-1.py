class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False
        else:
            unique="".join(dict.fromkeys(pattern))
            word=s.split()
            uni=dict.fromkeys(word)
            clean=" ".join(uni)
            if len(unique)==len(clean.split()):
                return True
            else:
                return False
            