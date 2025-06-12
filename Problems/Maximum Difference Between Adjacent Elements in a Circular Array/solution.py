import io
from typing import List
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxDist = -inf
        for i in range(n):
            maxDist = max(maxDist, abs(nums[i] - nums[(i + 1) % n]))

        return maxDist

obj = Solution()
#data = obj.maxAdjacentDistance(nums = [1,2,4])
data = obj.maxAdjacentDistance(nums = [-5,-10,-5])
print(data)