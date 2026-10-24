class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pair = []
        pa = []
        if len(nums) == 1:
            return True
        else:
            for i in range(0, len(nums) - 1):
                if (nums[i] % 2 == 0 and nums[i + 1] % 2 != 0) or (
                    nums[i] % 2 != 0 and nums[i+1] % 2== 0):
                    pa.append(nums[i])
                    pa.append(nums[i + 1])
                    pair.append(pa.copy())
                    pa.clear()
            if len(pair) == len(nums) - 1:
                return True
            else:
                return False
