class Solution:
    def maxDifference(self, s: str) -> int:
        odd = 0
        eve = float("inf")
        for i in set(s):
            a = s.count(i)
            if a % 2 == 0:
                if a < eve:
                    eve = a
            elif a % 2 != 0:
                if a > odd:
                    odd = a
        g=int(eve)
        return odd-g