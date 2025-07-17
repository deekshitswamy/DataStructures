import io
from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

        n = len(nums)
        res = 0
        for i in range(n):
            num = nums[i] % k
            for j in range(k):
                dp[j][num] = dp[num][j] + 1
                res = max(res, dp[j][num])
        return res

obj = Solution()
#data = obj.maximumLength(nums = [1,2,3,4,5], k = 2)
data = obj.maximumLength(nums = [1,4,2,3,1,4], k = 3)
print(data)