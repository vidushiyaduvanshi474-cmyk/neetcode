class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        con=0
        for i in words:
            if all(letter in allowed for letter in i):
                con+=1
        return con