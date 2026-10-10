class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        e=[]
        for i in emails:
            local,domain=i.split('@')
            if '+' in local:
                local=local.split('+')[0]
            local=local.replace('.','')
            clean=local+'@'+domain
            e.append(clean)
        t=set(e)
        return len(t)