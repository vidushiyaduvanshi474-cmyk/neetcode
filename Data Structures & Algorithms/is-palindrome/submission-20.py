import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "!@#$%^&*?/><"
        for i in r:
            s = s.replace(i, "")
        clean="".join(filter(str.isalnum,s)).lower()
        if clean==clean[::-1]:
            return True
        else:
            return False