from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out=0
        for i in words:
            if not (Counter(i)-Counter(chars)):
                out+=len(i)
        return out