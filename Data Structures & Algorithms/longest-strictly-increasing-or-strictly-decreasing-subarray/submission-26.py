class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = []
        dc = []
        g = []
        gg = []
        if len(set(nums)) == 1:
            return len(set(nums))
        else:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] > nums[i]:
                    if len(g) == 0:
                        g.append(nums[i])
                    g.append(nums[i + 1])
                else:
                    if len(g)>0:
                        inc.append(len(g))
                        g = []
                if nums[i + 1] < nums[i]:
                    if len(gg) == 0:
                        gg.append(nums[i])
                    gg.append(nums[i + 1])
                else:
                    if len(gg)>0:
                        dc.append(len(gg))
                        gg = []
            if len(gg)!=0:
                dc.append(len(gg))
            if len(g)!=0:
                inc.append(len(g))
        if len(inc) == 0:
            return max(dc)
        elif len(dc) == 0:
            return max(inc)
        else:
            return max(max(inc), max(dc))
