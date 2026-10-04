class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sen=0
        for i in details:
            if i[11:13].isdigit():
                t=int(i[11:13])
                if t>60:
                    sen+=1
        return sen
        