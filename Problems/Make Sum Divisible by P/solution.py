import io
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0

        currSumMod = 0
        res = len(nums)
        prefix_map = {0: -1}

        for i in range(0, len(nums)):
            currSumMod = (currSumMod + nums[i]) % p
            needMod = (currSumMod - remainder + p) % p

            if needMod in prefix_map:
                res = min(res, i - prefix_map[needMod])

            prefix_map[currSumMod % p] = i

        if res < len(nums):
            return res
        else:
            return -1

obj = Solution()
#data = obj.minSubarray(nums = [3,1,4,2], p = 6)
#data = obj.minSubarray(nums = [6,3,5,2], p = 9)
data = obj.minSubarray(nums = [1,2,3], p = 3)
print(data)