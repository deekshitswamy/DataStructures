import io
from math import inf
from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [inf] * n
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]

obj = Solution()
#data = obj.paintWalls(cost = [1,2,3,2], time = [1,2,3,2])
data = obj.paintWalls(cost = [2,3,4,2], time = [1,1,1,1])
print(data)